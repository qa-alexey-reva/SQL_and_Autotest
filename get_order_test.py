import sender_stand_request


def test_get_order():
    track = sender_stand_request.get_order_track()
    response = sender_stand_request.get_order(track)
    assert response.status_code == 200



    # Рева Алексей, 13-я кагорта
