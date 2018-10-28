genOption = (titleText, type, data) => {
    data = JSON.parse(data)
    let option = {}
    let item = {};
    switch (type) {
        case 'pie':
            let dataPieArray = []
            console.log(data)
            data.forEach(dataItem => {
                let item = {};
                console.log(dataItem)
                item.name = dataItem[0];
                item.value = dataItem[1];
                dataPieArray.push(item)
            })
            console.log(dataPieArray)
            option = {
                backgroundColor: '#fff',

                title: {
                    text: titleText,
                    left: 'center',
                    top: 20,
                    textStyle: {
                        color: '#ccc'
                    }
                },

                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b} : {c} ({d}%)"
                },

                visualMap: {
                    show: false,
                    min: 80,
                    max: 600,
                    inRange: {
                        colorLightness: [0, 1]
                    }
                },
                series: [
                    {
                        name: '访问来源',
                        type: 'pie',
                        radius: '55%',
                        center: ['50%', '50%'],
                        data: dataPieArray.sort(function (a, b) {
                            return a.value - b.value;
                        }),
                        roseType: '',
                        label: {
                            normal: {
                                textStyle: {
                                    color: 'rgba(0, 0, 0, 0.6)'
                                }
                            }
                        },
                        labelLine: {
                            normal: {
                                lineStyle: {
                                    color: 'rgba(0, 0, 0, 0.3)'
                                },
                                smooth: 0.2,
                                length: 10,
                                length2: 20
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: '#c23531', //color:'#3fa8f4',//color:'#ff921e',
                                shadowBlur: 100,
                                shadowColor: 'rgba(0, 0, 0, 0.2)'
                            }
                        },

                        animationType: 'scale',
                        animationEasing: 'elasticOut',
                        animationDelay: function (idx) {
                            return Math.random() * 200;
                        }
                    }
                ]
            };

            break;
        case 'bar':
            let dataBarAxis = []
            let dataBar = []
            let dataShadow = [];
            data.forEach(dataItem => {
                dataBarAxis.push(dataItem[0])
                dataBar.push(dataItem[1])
                dataShadow.push(500)
            })
            option = {
                title: {
                    text: titleText,
                    subtext: ''
                },

                tooltip: {
                    trigger: 'axis',

                },
                xAxis: {
                    data: dataBarAxis,
                    axisLabel: {
                        inside: false,
                        textStyle: {
                            color: '#666'
                        }
                    },
                    axisTick: {
                        show: false
                    },
                    axisLine: {
                        show: false
                    },
                    z: 10
                },
                yAxis: {
                    axisLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    },
                    axisLabel: {
                        textStyle: {
                            color: '#666'
                        }
                    }
                },

                series: [

                    {
                        type: 'bar',
                        itemStyle: {
                            normal: {
                                color: new echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [
                                        {offset: 0, color: '#83bff6'},
                                        {offset: 0.5, color: '#188df0'},
                                        {offset: 1, color: '#188df0'}
                                    ]
                                )
                            },
                            emphasis: {
                                color: new echarts.graphic.LinearGradient(
                                    0, 0, 0, 1,
                                    [
                                        {offset: 0, color: '#2378f7'},
                                        {offset: 0.7, color: '#2378f7'},
                                        {offset: 1, color: '#83bff6'}
                                    ]
                                )
                            }
                        },
                        data: dataBar
                    }
                ]
            };
            break;
        case 'bar2':
            let dataBar2Axis = []
            let dataBar2 = []
            let dataShadow2 = [];
            data.forEach(dataItem => {
                dataBar2Axis.push(dataItem[0])
                dataBar2.push(dataItem[1])
                dataShadow2.push(500)
            })
            option = {
                title: {
                    text: titleText,
                    subtext: ''
                },

                tooltip: {
                    trigger: 'axis',

                },
                yAxis: {
                    data: dataBar2Axis,
                    axisLabel: {
                        inside: false,
                        textStyle: {
                            color: '#666'
                        }
                    },
                    axisTick: {
                        show: false
                    },
                    axisLine: {
                        show: false
                    },
                    z: 10
                },
                xAxis: {
                    axisLine: {
                        show: false
                    },
                    axisTick: {
                        show: false
                    },
                    axisLabel: {
                        textStyle: {
                            color: '#666'
                        }
                    }
                },

                series: [

                    {
                        type: 'bar',
                        itemStyle: {
                            normal: {
                                color: new echarts.graphic.LinearGradient(
                                    1, 1, 0, 0,
                                    [
                                        {offset: 0, color: '#83bff6'},
                                        {offset: 0.5, color: '#188df0'},
                                        {offset: 1, color: '#188df0'}
                                    ]
                                )
                            },
                            emphasis: {
                                color: new echarts.graphic.LinearGradient(
                                    1, 1, 0, 0,
                                    [
                                        {offset: 0, color: '#2378f7'},
                                        {offset: 0.7, color: '#2378f7'},
                                        {offset: 1, color: '#83bff6'}
                                    ]
                                )
                            }
                        },
                        data: dataBar2
                    }
                ]
            };
            break;
        case 'line':
            let map = {};
            let title = [];
            let time = [];
            console.log(data);
            data.sort(function (x, y) {
                return x[1].localeCompare(y[1]);
            });
            data.sort(function (x, y) {
                return x[0] - y[0];
            });

            data.forEach((item, index) => {
                const key = item[1];
                if (!map[key]) {  // 按key来进行分类
                    map[key] = {
                        name: key,
                        type: 'line',
                        stack: '总量',
                        data: []
                    }
                    title.push(key)
                }
                if (time.indexOf(item[0]) === -1) {
                    time.push(item[0])
                }
                map[key].data.push(item[2]
                );
            })
            console.log(map)
            console.log(title)
            console.log(time)
            let aa = []
            title.map((t, i) => aa.push(map[t]))
            console.log(aa)
            option = {
                title: {
                    text: titleText,
                    left: 'center',
                    top: 20,
                    textStyle: {
                        color: '#ccc'
                    }
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: title
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis: {
                    type: '',
                    boundaryGap: false,
                    data: time
                },
                yAxis: {
                    type: 'value'
                },
                series: aa
            };
            break;
        case 'map':
            let seriesData = []
            data.forEach(dataItem => {
                item.name = dataItem[0];
                item.value = dataItem[1];
                seriesData.push(item)
            })
            option = {
                backgroundColor: '#FFFFFF',
                title: {
                    text: '全国地图大数据',
                    subtext: '',
                    x: 'center'
                },
                tooltip: {
                    trigger: 'item'
                },

                //左侧小导航图标
                visualMap: {
                    show: true,
                    x: 'left',
                    y: 'center',
                    splitList: [
                        {start: 500, end: 600}, {start: 400, end: 500},
                        {start: 300, end: 400}, {start: 200, end: 300},
                        {start: 100, end: 200}, {start: 0, end: 100},
                    ],
                    color: ['#5475f5', '#9feaa5', '#85daef', '#74e2ca', '#e6ac53', '#9fb5ea']
                },

                //配置属性
                series: [{
                    name: '数据',
                    type: 'map',
                    mapType: 'china',
                    roam: true,
                    label: {
                        normal: {
                            show: true  //省份名称
                        },
                        emphasis: {
                            show: false
                        }
                    },
                    data: seriesData  //数据
                }]
            };
            break;
        default:
            break;
    }
    return option
}
 fillChartBoxData = (chartBoxIdSelector, tabName) => {
    $.ajax({
        cache: false,
        type: "get",
        url: "{% url "policy: chartData" %}",
        data: {'tab': tabName},
        async: true,
        success: function (charts) {
            console.log(charts)
            let chartBoxId = chartBoxIdSelector.slice(1)
            $(chartBoxIdSelector).append('<h3>' + tabName + '</h3>')
            let i = 1;
            let chartsBoxTitle = '<ul class="nav nav-tabs">'
            let chartBoxTitle = ''
            charts.map((chart, idx) => {
                idx++;
                console.log('idx', idx)
                let chartTabId = chartBoxId + "Tab" + idx;
                let chartTabClass = "chartTab";
                if (idx === 1) {
                    chartBoxTitle = '<li id="' + chartTabId + '" class="' + chartTabClass + ' active"><a>' + chart.fields.tab2 + '</a></li>'

                } else {
                    chartBoxTitle = '<li id="' + chartTabId + '" class="' + chartTabClass + '"><a>' + chart.fields.tab2 + '</a></li>'

                }
                chartsBoxTitle += chartBoxTitle
            })
            chartsBoxTitle += '</ul>'
            $(chartBoxIdSelector).append(chartsBoxTitle)
            charts.forEach((chart) => {
                let chartId = chartBoxId + "-" + i;
                let chartClass = chartBoxId + ""
                let chartDiv = "<div id='" + chartId + "' class='" + chartClass + " ' style='height:300px;'></div>";
                $(chartBoxIdSelector).append(chartDiv)
                console.log(chartId, chartDiv)
                console.log(chart.fields.type, chart.fields.data)
                let theChart = echarts.init(document.getElementById(chartId));
                let option = genOption(chart.fields.title, chart.fields.type, chart.fields.data)
                theChart.setOption(option);
                if (i !== 1) {
                    $("#" + chartId).addClass('dispear');
                }
                i++;
            })
        },
    });

}

