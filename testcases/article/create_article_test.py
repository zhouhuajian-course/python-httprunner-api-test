# NOTE: Generated By HttpRunner v3.1.6
# FROM: har\article\create_article.har


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseCreateArticle(HttpRunner):

    config = Config("发帖接口测试").verify(False).base_url("${get_base_url()}")

    teststeps = [
        Step(
            RunRequest("/api/create_article")
            .post("/api/create_article")
            .with_headers(
                **{
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
                }
            )
            .with_cookies(
                **{"session": "${get_session_id()}"}
            )
            .with_data({"title": "测试标题", "content": "测试内容"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_greater_or_equals("body.data.article_id", 1)
        ),
    ]


if __name__ == "__main__":
    TestCaseCreateArticle().test_start()