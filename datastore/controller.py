from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class StreamExpression(object):
    operator: str
    first_operand: str
    second_operand: str = None


class Cache(object):
    def __init__(self) -> None:
        self.dict = {}

    def get_item(self, key: str) -> Union[None, str]:
        """Get value asscoiated with a key.

        :type key: str
        :rtype: Union[None, str]
        """
        return self.dict.get(key, None)

    def set_item(self, key: str, value: str) -> None:
        """Set value to a key.

        :type key: str
        :type value: str
        :rtype: None
        """
        self.dict[key] = value

    def delete_item(self, key: str) -> Union[None, str]:
        """Delete key/value pair.

        :type key: str
        :rtype: Union[None, str]
        """
        return self.dict.pop(key, None)


def validate_expression(expr: StreamExpression) -> bool:
    """Validate the input.

    :type expr: StreamExpression
    :rtype: bool
    """
    if expr.operator not in {'GET', 'SET', 'DELETE'}:
        return False

    if expr.operator in {'GET', 'DELETE'} and expr.second_operand is not None:
        return False
    elif expr.operator == 'SET' and expr.second_operand is None:
        return False

    return True


def evaluate_expression(
    operator,
    operand_a,
    operand_b: Optional[str] = None,
) -> Union[None, str]:
    """Evaluate the input.

    :type operator: str
    :type operand_a: str
    :type operand_b: str, optional
    :rtype: Union[None, str]
    """
    if operator == 'GET':
        return cache.get_item(operand_a)
    elif operator == 'SET':
        return cache.set_item(operand_a, operand_b)
    elif operator == 'DELETE':
        return cache.delete_item(operand_a)


def parse_input(request_str: str) -> Union[bool, None, str]:
    """Parse the input.

    :type request_str: str
    :rtype: Union[None, str]
    """
    expression = StreamExpression(
        *[part.decode('utf-8') for part in request_str.split()],
    )

    if not validate_expression(expression):
        print(expression)
        print('Invalid expression')
        return False

    return evaluate_expression(
        expression.operator,
        expression.first_operand,
        expression.second_operand,
    )


cache = Cache()
