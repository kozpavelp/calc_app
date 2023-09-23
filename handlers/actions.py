from fastapi import HTTPException


operators = ("+", "-", "*", "/")


async def calculate(x, y, operator):
    formula = f"{x} {operator} {y}"
    if operator in operators:
        if operator == "/" and y == 0:
            raise HTTPException(status_code=400, detail="Division by zero")
        else:
            result = eval(formula)
    else:
        raise HTTPException(status_code=400, detail="Wrong operator")
    return result
