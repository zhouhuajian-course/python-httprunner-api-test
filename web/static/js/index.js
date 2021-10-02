// 处理按钮点击
$('button').click(function() {
    $this = $(this)
    // 接口URL
    url = $this.attr('url')
    // AJAX调用接口
    if (url == '/api/login') {
        user = $this.parent().find("input[name=user]").val()
        pwd = $this.parent().find("input[name=pwd]").val()
        $.post(url, {user: user, pwd: pwd}, function(result) {
            alert(result.message)
        }, 'json')
    } else if (url == '/api/get_user_info') {
        $.get(url, function(result) {
            alert(result.message)
        }, 'json')
    } else if (url == '/api/logout') {
        $.post(url, function(result) {
            alert(result.message)
        }, 'json')
    } else if (url == '/api/create_article') {
        title = $this.parent().find("input[name=title]").val()
        content = $this.parent().find("textarea").val()
        $.post(url, {title: title, content: content}, function(result) {
            alert(result.message)
        }, 'json')
    } else if (url == '/api/del_article') {
        article_id = $this.parent().find("input[name=article_id]").val()
        $.post(url, {article_id: article_id}, function(result) {
            alert(result.message)
        }, 'json')
    }

})