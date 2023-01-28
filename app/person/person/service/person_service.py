from app.db import db
from app.ext import s3
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound
from app.person.person.entity.person_entity import PersonEntity
from app.person.person.schema.person_schema import (
    list_person_schema,
    person_schema,
    person_schema_out,
)
from ..model.person_dto import PersonDto
from app.subject.person_group.service.person_group_service import (
    activateSubject,
)
from app.subject.person_group.service.person_group_service import registered_person
from cloudinary.uploader import upload, destroy
from sqlalchemy.orm import joinedload
from ....subject.person_group.entity.person_group_entity import PersonGroupEntity
from sqlalchemy import or_

PersonEntity.start_mapper()


def findAll():
    try:
        persons = (
            db.session.query(PersonEntity)
            .options(
                joinedload(PersonEntity.person_group).joinedload(
                    PersonGroupEntity.group
                )
            )
            .all()
        )
        return list_person_schema.dump(persons)
    except NoResultFound:
        raise NoResultFound("no people registered yet")


def findOneByMail(term):
    try:
        person = (
            db.session.query(PersonEntity)
            .options(
                joinedload(PersonEntity.person_group).joinedload(
                    PersonGroupEntity.group
                )
            )
            .filter(
                or_(PersonEntity.institutional_mail == term, PersonEntity.code == term)
            )
            .one()
        )
        return person_schema_out.dump(person)
    except NoResultFound:
        raise NoResultFound(f"The person with search term {term} does not exist")


def findTeachers():
    teachers = db.session.query(PersonEntity).filter(PersonEntity.role_id == 1).all()
    if not teachers:
        raise NoResultFound("no teachers registered yet")
    return list_person_schema.dump(teachers)


def create(data):
    person = None
    try:
        person = person_schema.load(data)
        db.session.add(
            PersonDto(
                institutional_mail=person["institutional_mail"],
                names=person["names"],
                lastnames=person["lastnames"],
                code=person["code"],
                document_type_id=person["document_type_id"],
                role_id=person["role_id"],
            )
        )
        db.session.commit()
        return person
    except ValidationError as error:
        raise ValidationError(error.messages)
    except Exception as error:
        raise Exception(error.args)


def registerInCourse(data):
    try:
        if get_person_of_subject(
            data
        ):  # SOLO ME MUESTRA LOS GRUPOS QUE LA PERSONA TENGA ACTIVOS CANCELLD:FALSE Y STATE: IN_PROCESS
            return {"msg": "the person is already registered in the matter"}
        else:
            exist = activateSubject(  # SI YA ESTABA PERO LA HABIA PERDIDO O CANCELADO ENTONCES ACTIVAMOS LA MATERIA
                data["person_id"], data["group_id"]
            )
            if exist:
                return "successfully registered person"
            else:
                return registered_person(data)
    except Exception as error:
        raise Exception(error.args)


def get_person_of_subject(data):
    try:
        exist = (
            db.session.query(PersonEntity)
            .options(
                joinedload(PersonEntity.person_group).joinedload(
                    PersonGroupEntity.group
                )
            )
            .filter(PersonEntity.institutional_mail == data["person_id"])
            .one()
        )
        for info in exist.person_group:
            if (
                info.group.id == data["group_id"]
                and info.group.subject_id == data["subject_id"]
                and info.cancelled == False
            ):
                return True
        return False
    except NoResultFound:
        raise NoResultFound(f"no exist person with email {data['institutional_mail']}")


def updateImage(file, mail):
    try:
        image = (
            db.session.query(PersonEntity)
            .filter(PersonEntity.institutional_mail == mail)
            .one()
        )
        print(image.img)
        if image.img != "":
            url = image.img.split("/")
            id_img = url[-1].split(".")
            destroy(f"classroom-projects/{id_img[0]}")
        response = upload(file, folder="classroom-projects")
        image.img = response["url"]
        db.session.commit()
        return image.img
    except NoResultFound as error:
        raise NoResultFound(f"no exist person with email {mail}")
    except Exception as error:
        raise Exception(error.args)


# * TODO: VOY A UTILIZAR MEJOR CLOUDINARY POR TEMAS DE COSTOS
# def UpdateImage(file,mail):
#     print(file, mail)
#     s3.upload_file(file.filename, "ayd-project", file.filename)
#     s3.put_object_acl(Bucket="ayd-project", Key=file.filename, ACL='public-read')
#     url = s3.generate_presigned_post("ayd-project", file.filename)

#     os.remove(file.filename)
#     return {"msg":url}
