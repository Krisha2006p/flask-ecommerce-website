from decimal import Decimal

from sqlalchemy import Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.extensions import db

class Product(db.Model):  # db.Model tells SQLAlchemy that this class represents a database model.
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        primary_key = True)

    name: Mapped[str] = mapped_column(
        db.String(100),
        nullable = False)

    price: Mapped[Decimal] = mapped_column(  # Example: Decimal("499.50"), use Decimal rather than a regular Python float for money because floating-point arithmetic can introduce small precision errors.
        # Floating-point arithmetic introduces representation errors because standard computers store float data types using binary (base-2) fractions rather than decimal (base-10) numbers.
        # Because of this architectural difference, many clean, finite decimal numbers cannot be represented exactly in binary, leading to infinite repeating fractions that must be cut off and rounded.
        # For example, the number 0.1 is actually stored by a regular Python float as roughly 0.10000000000000000555111512...
        Numeric(10, 2),   # a number with up to 10 total digits, including 2 after the decimal point.
        nullable = False)

    description: Mapped[str | None] = mapped_column(
        db.String(500),
        nullable = True)

    stock: Mapped[int] = mapped_column(
        nullable = False,
        default = 0)

    image_filename: Mapped[str | None] = mapped_column(  # value can be a filename or None.
        db.String(255),
        nullable = True   # allows the database field to be empty.
    )