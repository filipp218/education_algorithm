async def test_post_favoriteway(cli, db):
    resp = await cli.post(
        '/favoriteway/100',
        json={
            "location1": {
                "lat": 56.7448873,
                "long": 49.1811542
            },
            "location2": {
                "lat": 55.74550,
                "long": 49.189232
            },
            "install_date": "2021-06-30 12:42:10.940759"
        }
    )
    assert resp.status == 201
    text = await resp.json()
    validator = jsonschema.Draft7Validator(favorite_way_post201)
    assert validator.is_valid(text)

    resp = await cli.post(
        '/favoriteway/100',
        json={
            "location1": {
                "lat": 56.7448873,
                "long": 49.1811542
            },
            "location2": {
                "lat": 55.74550,
                "long": 49.189232
            },
            "install_date": "2021-06-30 12:42:10.940759"
        }
    )
    assert resp.status == 400
    text = await resp.json()
    validator = jsonschema.Draft7Validator(favorite_way_post400)
    assert validator.is_valid(text)
