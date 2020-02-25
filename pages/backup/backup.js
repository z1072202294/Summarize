Page({
    data: {
      // 待上传的文件列表
        files: [],
        // 下载的文件列表
        downloadFiles:[]
    },
    chooseImage: function (e) {
        var that = this;
        wx.chooseImage({
            sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
            sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
            success: function (res) {
                // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
                that.setData({
                    files: that.data.files.concat(res.tempFilePaths)
                });
            }
        })
    },
    previewImage: function(e){
        wx.previewImage({
            current: e.currentTarget.id, // 当前显示图片的http链接
            urls: this.data.files // 需要预览的图片http链接列表
        })
    },
    // 上传图片
  uploadFiles: function(){
    for (var i=0; i < this.data.files.length; i++){
      var filePath = this.data.files[i]
      wx.uploadFile({
        url: 'http://127.0.0.1:8000/api/v1.0/service/imageview',
        filePath: filePath,
        name: 'test',
        success: function(res) {
          console.log(res.data)
        }
      })
    }
  },
    // 下载图片
  downloadFile: function (ImgItem) { 
    // console.log(ImgItem)
    var that = this
    wx.downloadFile({
      url:'http://127.0.0.1:8000/api/v1.0/service/imageview?md5=e1fbc54c9bc413e82bba4951053f7cf4.jpg',
      success:function(res){
        console.log(res.errMsg)
        console.log(res.tempFilePath)
        console.log(res.statusCode)
        var tmpPath = res.tempFilePath
        var newDownLoadFiles = that.data.downloadFiles
        newDownLoadFiles.push(tmpPath)
        that.setData({
          downloadFiles:newDownLoadFiles
        })

      }
    })
  },
    // 删除图片(服务器)
  deleteBackup: function (ItemImage) {
    wx.request({
      url: '',
      method:'DELETE',
      success: function(res){
        
      }
    })
   },
  //  删除图片(本地)
  longTapConfirm: function(e){
    var that = this
    wx.showActionSheet({
      itemList: ['删除这张图片'],
      success: function(res){
        if(res.cancel){
          return
        }
        var imageIndex = e.currentTarget.dataset.index
        var imageItem = that.data.downloadFiles[imageIndex]
        var newList = that.data.downloadFiles
        newList.splice(imageIndex,1)
        that.setData({
          downloadFiles:newList
        })
        
      }
    })
  }
});