class User:
    _id_ = 0

    def __init__(self, name, age, email) -> None:
        self.name = name
        self.age = age
        self.email = email
        User._id_ += 1
        self.id = User._id_

    def __str__(self):
        return f"{self.name}"
