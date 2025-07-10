from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from typing import Optional


class PaymentModel(BaseModel):
    id: Optional[int] = None
    user_id: UUID
    status: str
    valid_until: datetime
    payed_at: datetime
    tariff_id: int
    amount: int
    currency: str
    balance: int
    payment_id: Optional[str] = None  # Changed to string to match database varchar type
