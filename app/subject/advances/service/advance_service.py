from app.db import db
from marshmallow import ValidationError
from ..schema.advance_schema import advance_schema
from ..model.advance_dto import AdvanceDto
from ..entity.advances_entity import AdvanceEntity

AdvanceEntity.start_mapper()

def createAdvance(data):
    advance = None
    try:
        advance = advance_schema.load(data)
        db.session.add(
            AdvanceDto(
                name=advance["name"],
                description=advance["description"],
                link=advance["link"],
                delivery_date=advance["delivery_date"],
                state=advance["state"],
                project_id=advance["project_id"],
            )
        )
        db.session.commit()
        return advance
    except ValidationError as e:
        raise ValidationError(e.messages)
    except Exception as e:
        raise Exception(e.args)
