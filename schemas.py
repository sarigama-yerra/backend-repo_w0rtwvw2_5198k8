"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Business-specific schemas for the Window Cleaning website

class ContactMessage(BaseModel):
    """
    General contact messages from the website
    Collection name: "contactmessage"
    """
    name: str = Field(..., description="Sender full name", min_length=2)
    email: EmailStr = Field(..., description="Sender email address")
    phone: Optional[str] = Field(None, description="Optional phone number")
    subject: Optional[str] = Field(None, description="Message subject")
    message: str = Field(..., description="Message body", min_length=5)

class QuoteRequest(BaseModel):
    """
    Free quote requests from potential clients
    Collection name: "quoterequest"
    """
    name: str = Field(..., description="Requester full name", min_length=2)
    email: EmailStr = Field(..., description="Requester email")
    phone: Optional[str] = Field(None, description="Phone number")
    company: Optional[str] = Field(None, description="Company/organization name")
    location: str = Field(..., description="Site location / address")
    property_type: str = Field(..., description="Type of property (mall, office, storefront, etc.)")
    approx_windows: Optional[int] = Field(None, ge=0, description="Approximate number of windows/panes")
    frequency: Optional[str] = Field(None, description="Desired cleaning frequency")
    notes: Optional[str] = Field(None, description="Additional details")

# Example schemas retained for reference (not used directly by the app)
class User(BaseModel):
    name: str
    email: str
    address: str
    age: Optional[int] = None
    is_active: bool = True

class Product(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    category: str
    in_stock: bool = True
