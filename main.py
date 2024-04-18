from typing import Union

from fastapi import FastAPI

import  json
import random


app = FastAPI()
exp = [1, "Name"]
pizzas = [
    {
        "name": "Margherita",
        "description": "Traditional pizza recipe with Mozzarella, juicy tomatoes, signature tomato sauce and oregano.",
        "calories": 900,
        "price": 9.99,
        "available": True
    },

    {
        "name": "Pepperoni Pizza",
        "description": "Classic pizza topped with delicious pepperoni slices.",
        "calories": 280,
        "price": 12.99,
        "available": True
    },

    {
        "name": "Hawaiian Pizza",
        "description": "Sweet and savory pizza topped with ham, pineapple, and mozzarella cheese.",
        "calories": 300,
        "price": 11.99,
        "available": True
    },

    {
        "name": "Veggie Supreme Pizza",
        "description": "Loaded with assorted vegetables like bell peppers, onions, olives, and mushrooms.",
        "calories": 270,
        "price": 12.49,
        "available": True
    },

    {
        "name": "BBQ Chicken Pizza",
        "description": "Tangy barbecue sauce, grilled chicken, red onions, and cilantro atop a cheesy crust.",
        "calories": 320,
        "price": 13.49,
        "available": False
    },

    {
        "name": "Meat Pizza",
        "description": "Packed with various meats such as pepperoni, sausage, bacon, and ham.",
        "calories": 350,
        "price": 14.99,
        "available": False
    },

    {
        "name": "Four Cheese Pizza",
        "description": "A blend of four cheeses - mozzarella, cheddar, parmesan, and provolone.",
        "calories": 280,
        "price": 12.99,
        "available": True
    },

    {
        "name": "Mushroom Truffle Pizza",
        "description": "Creamy truffle sauce with sautéed mushrooms, finished with parmesan and parsley.",
        "calories": 290,
        "price": 13.99,
        "available": True
    },

    {
        "name": "Spinach and Feta Pizza",
        "description": "Fresh spinach and tangy feta cheese on a garlic-infused crust.",
        "calories": 260,
        "price": 11.99,
        "available": False
    },

    {
        "name": "Buffalo Chicken Pizza",
        "description": "Spicy buffalo sauce, grilled chicken, red onions, and blue cheese crumbles.",
        "calories": 330,
        "price": 13.49,
        "available": True
    },

    {
        "name": "Supreme Pizza",
        "description": "The ultimate pizza experience with a combination of meats, vegetables, and extra cheese.",
        "calories": 380,
        "price": 15.49,
        "available": True
    }
]


@app.get("/pizza")
def read_pizza():

    return random.choice(pizzas)

print(exp)
