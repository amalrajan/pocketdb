from dataclasses import dataclass
from typing import Optional, Union

from logzero import logger


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
        if key not in self.dict:
            logger.debug(f'Key not found: {key}')

        return self.dict.get(key, None)

    def set_item(self, key: str, value: str) -> None:
        """Set value to a key.

        :type key: str
        :type value: str
        :rtype: None
        """
        if key in self.dict:
            logger.debug(
                f'Updating {key} with '
                ' {self.dict.get(key)} -> {value}',
            )
        else:
            logger.debug(f'Seting {key} -> {value}')
        self.dict[key] = value

    def delete_item(self, key: str) -> Union[None, str]:
        """Delete key/value pair.

        :type key: str
        :rtype: Union[None, str]
        """
        if key not in self.dict:
            logger.debug(f'Key not found: {key}')
        else:
            logger.debug(
                f'Deleting {key} -> {self.dict[key]}',
            )
        return self.dict.pop(key, None)


def validate_expression(expr: StreamExpression) -> bool:
    """Validate the input.

    :type expr: StreamExpression
    :rtype: bool
    """
    if expr.operator not in {'GET', 'SET', 'DELETE'}:
        logger.error(f'Invalid operator: {expr.operator}')
        return False

    if expr.operator in {'GET', 'DELETE'} and expr.second_operand is not None:
        logger.error('Too many values to unpack. Expected 1, found 2')
        return False
    elif expr.operator == 'SET' and expr.second_operand is None:
        logger.error('Not enough values to unpack. Expected 2, found 1')
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
        logger.error(f'Invalid expression: {expression}')
        return False

    return evaluate_expression(
        expression.operator,
        expression.first_operand,
        expression.second_operand,
    )


cache = Cache()
