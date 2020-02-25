// pages/apps/apps.js
const app = getApp()
Page({
  /**
   * 页面的初始数据
   */
  data: {
    grids: ['应用1','应用2']

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.updataMenuDate()

  },
  updataMenuDate: function () {
    var that = this
    wx.request({
      url: 'http://127.0.0.1:8000/api/v1.0/service/menu',
      success: function (res) {
        // console.log(res)
        var menuData = res.data.data
        that.setData({
          grids:menuData
        })
      },
      fail: function (res) {
        console.log('失败')
      }
    })

  },
  onNavigatorTap:function(e){
    var menuIndex = e.currentTarget.dataset.index
    var gridsItem = this.data.grids[menuIndex]

    // console.log(menuIndex,gridsItem)
    if(gridsItem.app.application =='Weather'){
      // 天气
      console.log(gridsItem.app.application)
      wx.navigateTo({
        url: '/pages/weather/index',
      })
    } else if (gridsItem.app.application == 'WeChat'){
      // 微信
      console.log(gridsItem.app.application)
      wx.navigateTo({
        url: '/pages/wx/index',
      })
    } else if (gridsItem.app.application == 'Alipay') {
      // 支付宝
      console.log(gridsItem.app.application)
      wx.navigateTo({
        url: '/pages/zfb/index',
      })
    }  else if (gridsItem.app.application == 'Joke') {
        // 支付宝
        console.log(gridsItem.app.application)
        wx.navigateTo({
          url: '/pages/Joke/index',
        })
    }
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})