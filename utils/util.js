const formatTime = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  return [year, month, day].map(formatNumber).join('/') + ' ' + [hour, minute, second].map(formatNumber).join(':')
}

const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : '0' + n
}
// 设置一个常量
const key = 'cookie'
// 1 从后台获取 session(cookies)
// 2 把 cookies 保存到本地
// 3 从本地 把 cookies 读取出来,以便于携带 cookies 到后台

function getSessionIDFromResponse(res){
  console.log(res)
  var cookie = res.header['Set-Cookie']
  console.log('getSessionIDFromResponse : '+cookie)
  return cookie
}
function setCookiesToStorage(cookie){
  try{
    wx.setStorageSync(key, cookie)
  }catch(e){
    console.log(e)
  }
}
function getCookiesTostorage(){

}
module.exports = {
  formatTime: formatTime,
  getSessionIDFromResponse: getSessionIDFromResponse,
  setCookiesToStorage: setCookiesToStorage,
  getCookiesTostorage: getCookiesTostorage

}
