// pages/Login/login.js
const cookies = require('../../utils/util.js')
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },
  getCooikes:function(){
    wx.request({
      url: 'http://127.0.0.1:8000/api/v1.0/service/session',
      success: function(res){
        var cookie = cookies.getSessionIDFromResponse(res)
        console.log(cookie)
        cookies.setCookiesToStorage(cookie)
      }
    })
  },
  sendCookie:function(){
    var cookie = cookies.getCookiesTostorage()
    var headers = {}
    headers.Cookie = cookie
    wx.request({
      url: 'http://127.0.0.1:8000/api/v1.0/service/cookie',
      header: headers,
      success: function(res){
        console.log(res)
        console.log(res.data)
      }
    })
  },
  authorize:function(){
    wx.login({
      success: function(res) {

        wx.request({
          url: 'http://127.0.0.1:8000/api/v1.0/service/authorize',
          method: 'POST',
          data:{
            code:res.code,
            nickname: app.globalData.userInfo.nickName
          },
          success: function(res){
            wx.showToast({
              title: '认证成功',
            })
            // 获取返回来的 session
            var cookie = cookies.getSessionIDFromResponse(res)
            console.log(cookie)
            cookies.setCookiesToStorage(cookie)
            console.log(app.globalData.userInfo)
          }
        })
      },
      fail: function(res) {},
      complete: function(res) {},
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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