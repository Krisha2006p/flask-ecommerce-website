from flask import Blueprint, render_template, request, redirect, url_for, current_app # lets us access the active Flask application's settings, including its static folder.
from app.models import Product
from decimal import Decimal
from app.extensions import db
import os   # helps us create and work with file paths.
from werkzeug.utils import secure_filename  # cleans up a filename supplied by the user so it is safer to use as a filename.
from uuid import uuid4  # generate random ID for product image filename (which is store in the uploads folders)

ALLOWED_IMAGE_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}

def allowed_image(filename):
    return (
        "." in filename # checks whether the filename contains a dot.
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS # splits the filename at the last dot and gets the extension.
    )

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/products")
def products():
    p = Product.query.all()
    return render_template("products.html", items = p)

@main.route("/admin/products/add", methods=['GET', 'POST'])  # GET: When we open /admin/products/add, Flask displays the form. , POST: When we click the Add Product button, Flask receives the submitted values.
def add_product():
    if request.method == "POST":
        # 1. Grab the form data using the input field 'name' attributes
        p_name = request.form.get('product_name')
        p_price = request.form.get('price')
        p_description = request.form.get('description')
        p_stock = request.form.get('stock')
        p_image = request.files.get('product_image')
        image_filename = None

        if p_image and p_image.filename:
            original_filename = secure_filename(p_image.filename)

            # secure_filename usage:
            # Original filename ->	After secure_filename()
            # phone.jpg	            phone.jpg
            # My New Phone.jpg	    My_New_Phone.jpg
            # ../../secret.jpg	    secret.jpg
            # It cleans the filename to make it safer to use as a filesystem name.

            if not allowed_image(original_filename):
                return "Invalid image type. Use JPG, JPEG, PNG, or WEBP.", 400

            extension = original_filename.rsplit(".", 1)[1].lower()
            image_filename = f"{uuid4().hex}.{extension}"  # uuid4().hex generates a unique filename.

            upload_folder = os.path.join(
                current_app.root_path, "static", "uploads"
            )
            os.makedirs(upload_folder, exist_ok=True)  # creates the folder if it doesn't exist.

            p_image.save(os.path.join(upload_folder, image_filename))

        # As we get the form data into a string formate so we need to convert it into an appropriate formate:
        p_price = Decimal(p_price)
        p_stock = int(p_stock)

        product = Product(
            name = p_name,
            price = p_price,
            description = p_description,
            stock = p_stock,
            image_filename = image_filename
        )

        db.session.add(product) # it's like putting product into a list of changes to save
        db.session.commit() # here we are actually saving it in DB.

        return redirect(url_for("main.products")) # products function inside main blueprint
    return render_template("add_product.html")  # GET displays the form.
