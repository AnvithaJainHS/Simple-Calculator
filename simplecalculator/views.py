"""View to calculate the result."""

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import CalculatorSerializer


class CalculatorAPIView(CreateAPIView):
    """View to get result."""

    serializer_class = CalculatorSerializer

    def post(self, request) -> Response:
        """Get result from request data."""
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            number1 = serializer.validated_data["number1"]
            number2 = serializer.validated_data["number2"]
            operation = serializer.validated_data["operation"]

            if operation == "add":
                result = number1 + number2
            elif operation == "subtract":
                result = number1 - number2
            elif operation == "multiply":
                result = number1 * number2
            elif operation == "divide":
                if number2 != 0:
                    result = number1 / number2
                else:
                    return Response(
                        {"error": "Cannot divide by zero"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response({"error": "Invalid Operation"})
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
