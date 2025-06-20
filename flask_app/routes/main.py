from flask import Blueprint, render_template, redirect, flash
from forms.expense_form import ExpenseForm
from models.db import collection
from utils.user import User
main = Blueprint("main", __name__)

# Constants (put this near the top of your file)
EXPENSE_CATEGORIES = ["utilities", "entertainment",
                      "school_fees", "shopping", "healthcare"]


@main.route("/", methods=["GET", "POST"])
def index():
    form = ExpenseForm()
    if form.validate_on_submit():
        # Define all categories
        EXPENSE_CATEGORIES = ["utilities", "entertainment",
                              "school_fees", "shopping", "healthcare"]

        # Initialize base data
        data = {
            "age": form.age.data,
            "gender": form.gender.data,
            "income": form.income.data,
            "expenses": {}
        }

        # Ensure all expense categories are always included
        for category in EXPENSE_CATEGORIES:
            checkbox_field = getattr(form, category)
            amount_field = getattr(form, f"{category}_amount")
            data["expenses"][category] = amount_field.data if checkbox_field.data else 0.0

        # Save to MongoDB
        result = collection.insert_one(data)

        # Create User and write to CSV
        user = User(
            id=result.inserted_id,
            age=form.age.data,
            gender=form.gender.data,
            income=form.income.data,
            expenses=data["expenses"]
        )
        User.write_to_csv([user])
        flash("Data submitted successfully!", "success")
        return redirect("/")

    return render_template("form.html", form=form)
