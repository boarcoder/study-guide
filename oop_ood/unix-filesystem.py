from abc import abstractmethod


class File:
    def __init__(self, name, children=[]):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children


class Specification:
    def and_specification(self, candidate):
        raise NotImplementedError()

    def or_specification(self, candidate):
        raise NotImplementedError()

    def not_specification(self, candidate):
        raise NotImplementedError()

    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass


class CompositeSpecification(Specification):
    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass

    def and_specification(self, candidate):
        return AndSpecification(self, candidate)

    def or_specification(self, candidate):
        return OrSpecification(self, candidate)

    def not_specification(self):
        return NotSpecification(self)


class AndSpecification(CompositeSpecification):
    def __init__(self, one, other):
        self._one: Specification = one
        self._other: Specification = other

    def is_satisfied_by(self, candidate):
        return bool(
            self._one.is_satisfied_by(candidate)
            and self._other.is_satisfied_by(candidate)
        )


class OrSpecification(CompositeSpecification):
    def __init__(self, one, other):
        self._one: Specification = one
        self._other: Specification = other

    def is_satisfied_by(self, candidate):
        return bool(
            self._one.is_satisfied_by(candidate)
            or self._other.is_satisfied_by(candidate)
        )
