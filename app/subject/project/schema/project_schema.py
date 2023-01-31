from app.ext import ma
from marshmallow import fields, validate, post_load


class ProjectSchema(ma.Schema):

    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(min=3, max=50))
    description = fields.String(required=True)
    active = fields.Boolean(default=True)
    number_of_students = fields.Integer(required=True)

    """
    * estados permitidos
    * on_hold = EN ESPERA --> ESTADO POR DEFECTO HASTA QUE EL PROFESOR LO CAMBIE A IN_PROCESS
    * in_process = EN PROCESO --> PASA A IN_PROCCESS CUANDO EL PROFESOR LO ACTIVE
    * finished = FINALIZADO,
    * proposal = PROPUESTA
    """
    state = fields.String(
        validate=validate.OneOf(["in_process", "finished", "proposal", "on_hold"]),
    )
    full = fields.Boolean(
        default=False
    )  # * 👀 ESTE CAMBIA CUANDO YA SE TIENE LA CANTIDAD DE ESTUDIANTES MAXIMA

    advance = fields.Nested('AdvanceSchema', many=True, only=('name', 'description', 'link')) 
    
    group_id = fields.Integer(required=True)
    person_project = fields.Nested("PersonProjectSchema", many=True, only=('person',))

    @post_load
    def lower_names(self, in_data, **kwargs):
        in_data["name"] = in_data["name"].lower().strip()
        in_data["description"] = in_data["description"].lower().strip()
        return in_data


project_schema = ProjectSchema()
list_project_schema = ProjectSchema(many=True)
list_project_without_persons_schema = ProjectSchema(many=True, exclude=("person_project",))
