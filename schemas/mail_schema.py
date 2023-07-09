from pydantic import BaseModel


class MailTrackingNumber(BaseModel):
    mail_to: str
    order_id: int
    tracking_number: str


class MailFormCourses(BaseModel):
    name: str
    email: str
    phone: str
    course: str
    option: str
