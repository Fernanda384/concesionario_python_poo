from abc import abstractmethod
class Vehiculo:
    def __init__(self, marca: str, modelo: str, precio_base: float):
        self._marca = marca
        self._modelo = modelo
        self._precio_base = float(precio_base)

    def get_marca(self) -> str:
        return self._marca

    def get_modelo(self) -> str:
        return self._modelo

    def get_precio_base(self) -> float:
        return self._precio_base

    @abstractmethod
    def impuesto(self) -> float:
        """Método que debe ser implementado por subclases para calcular impuesto."""
        raise NotImplementedError("Subclase debe implementar impuesto()")

    def __str__(self) -> str:
        return f"Marca: {self._marca}, Modelo: {self._modelo}, Precio base: {self._precio_base:.2f}"
