from app.db import db
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound
from cloudinary.uploader import upload
from ..schema.advance_schema import advance_schema
from ..model.advance_dto import AdvanceDto
from ..entity.advances_entity import AdvanceEntity
from ...project.service.project_service import findOneProject

AdvanceEntity.start_mapper()


def createAdvance(data):
    advance = None
    try:
        advance = advance_schema.load(data)
        findOneProject(advance['project_id'])
        db.session.add(
            AdvanceDto(
                name=advance["name"],
                description=advance["description"],
                delivery_date=advance["delivery_date"],
                project_id=advance["project_id"],
            )
        )
        db.session.commit()
        return advance
    except ValidationError as e:
        raise ValidationError(e.messages)
    except Exception as e:
        raise Exception(e.args)


def findOneById(id):
    try:
        advance = db.session.query(AdvanceEntity).filter_by(id=id).one()
        return advance_schema.dump(advance)
    except NoResultFound:
        raise Exception(f"advance with id {id} not found")

#* OJO SOLOMENTE PUEDE HACER UNA ENTREGA
def uploadFile(id, file):
    try:
        advance = (
            db.session.query(AdvanceEntity)
            .filter_by(id=id)
            .one()
        )            
        response = upload(file, resource_type="auto", folder="classroom-projects", format="zip")
        advance.link = response["url"]
        advance.state = True
        db.session.commit()
        return advance.link
    except NoResultFound as error:
        raise NoResultFound(f"advance with id {id} not found")
    except Exception as error:
        raise Exception(error.args)