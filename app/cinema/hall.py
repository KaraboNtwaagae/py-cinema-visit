from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list[Customer],
            cleaning_staff: Cleaner
    ) -> None:
        print(
<<<<<<< HEAD
            f'"{movie_name}" started in hall number'
            f"{self.number}."
=======
            f'"{movie_name}" started in hall number '
            f'{self.number}.'
>>>>>>> 344d963d16a1f1c79ef1449dc4c096819df747fd
        )

        for customer in customers:
            customer.watch_movie(movie_name)

        print(f'"{movie_name}" ended.')

        cleaning_staff.clean_hall(self.number)
