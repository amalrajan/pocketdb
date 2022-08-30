from typing import List
from dataclasses import dataclass


@dataclass
class StreamExpression(object):
    operator: str
    first_operand: str
    second_operand: str = None


class Cache(object):
    def __init__(self) -> None:
        self.dict = {}

    def get_item(self, key: str) -> str:
        return self.dict.get(key, None)

    def set_item(self, key: str, value: str) -> bool:
        self.dict[key] = value

    def delete_item(self, key: str) -> bool:
        self.dict.pop(key, None)


def validate_expression(expr: StreamExpression) -> bool:    
    if expr.operator not in {'GET', 'SET', 'DELETE'}:
        return False

    if expr.operator in {'GET', 'DELETE'} and expr.second_operand is not None:
        return False

    if expr.operator == 'SET' and expr.second_operand is None:
        return False

    return True


def evaluate_expression(operator, operand_a, operand_b=None):
    if operator == 'GET':
        return cache.get_item(operand_a)
    elif operator == 'SET':
        return cache.set_item(operand_a, operand_b)
    elif operator == 'DELETE':
        return cache.delete_item(operand_a)


def parse_input(request_str: str):
    expression = StreamExpression(
        *[part.decode('utf-8') for part in request_str.split()]
    )

    if not validate_expression(expression):
        print(expression)
        print('Invalid expression')
        return False

    return evaluate_expression(
            expression.operator,
            expression.first_operand,
            expression.second_operand
        )

cache = Cache()
