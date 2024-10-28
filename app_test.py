from app import process_query


def test_knows_about_dinosaurs():
    expected = "Dinosaurs ruled the Earth 200 million years ago"
    assert process_query("dinosaurs") == expected


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_for_name():
    assert process_query("What is your name?") == "Team_Wun"


def test_for_addition():
    assert process_query("What is 37 plus 38?") == "75"


def test_for_multiplication():
    assert (
        process_query(
            "What is 81 multiplied\
     by 39?"
        )
        == "3159"
    )


def test_for_largest():
    assert (
        process_query(
            "Which of the following numbers\
         is the largest: 67, 28, 23?"
        )
        == "67"
    )
