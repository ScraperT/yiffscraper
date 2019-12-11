import yiff

projid = "7330723"
projname = "Belle Delphine"
projpatreonurl = "https://www.patreon.com/belledelphine"
projyiffurl = "http://yiff.party/patreon/7330723"


# TODO: Find a mock out the downloads, so running these tests don't take forever
# def test_scrapeFromPatreonId():
#     yiff.scrape(projid)
#     # TODO: Check result


# def test_scrapeFromPatreonUrl():
#     yiff.scrape(projpatreonurl)
#     # TODO: Check result


# def test_scrapeFromYiffUrl():
#     yiff.scrape(projyiffurl)
#     # TODO: Check result


def test_initSession():
    s = yiff.initSession()
    assert s.cookies.get("party", domain="yiff.party") is not None


def test_getProjectInfoFromPatreonId():
    info = yiff.getProjectInfo(projid)
    assert info.id == projid
    assert info.name == projname
    assert info.patreonurl == projpatreonurl
    assert info.yiffurl == projyiffurl


def test_getProjectInfoFromPatronUrl():
    info = yiff.getProjectInfo(projpatreonurl)
    assert info.id == projid
    assert info.name == projname
    assert info.patreonurl == projpatreonurl
    assert info.yiffurl == projyiffurl


def test_getProjectInfoFromYiffUrl():
    info = yiff.getProjectInfo(projyiffurl)
    assert info.id == projid
    assert info.name == projname
    assert info.patreonurl == projpatreonurl
    assert info.yiffurl == projyiffurl