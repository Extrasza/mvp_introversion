from pydantic import BaseModel, Field

from pydantic import BaseModel, Field

class PersonalitySchema(BaseModel):
    Time_spent_Alone: float = Field(..., example=6)
    Stage_fear: bool = Field(..., example=True)
    Social_event_attendance: float = Field(..., example=3)
    Going_outside: float = Field(..., example=2)
    Drained_after_socializing: bool = Field(..., example=False)
    Friends_circle_size: float = Field(..., example=3)
    Post_frequency: float = Field(..., example=2)

class PersonalityResultSchema(BaseModel):
    resultado: str = Field(..., example="Introvertido")

class ErrorSchema(BaseModel):
    message: str = Field(..., example="Erro ao classificar personalidade")