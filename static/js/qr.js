$('.ask').on('click', function () {
    layer.open({
        type: 1,
        title: false,
        closeBtn: 1,
        area: '431px',
        skin: 'layui-layer-nobg', //没有背景色
        shadeClose: true,
        content: $('#qr')
    });
});