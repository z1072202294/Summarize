// pages/Joke/index.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    contents:[]
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this
    wx.request({
      url: 'http://v.juhe.cn/joke/content/list.php?sort=desc&page=10&pagesize=10&time=1582527736&key=f1956f725c237b265928531a3b0f416a',
      success: function (res) {
        // console.log(res.data.result)
        that.setData({
          contents: res.data.result.data
        })
        console.log(that.data.contents)
      }
    })
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