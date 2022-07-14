const cams = 1
const ip = 'http://ipgohere/'
const mode = 'foscam'


document.addEventListener('DOMContentLoaded', () => {
    let container = document.getElementById('video-grid-container')
    for(let i = 1; i <= cams; i++) {
        let div = document.createElement('img')
        div.setAttribute('id', `video-${i}`)
        container.appendChild(div)
    }
    // while(true) {
    let func = () => {for(let i = 1; i <= cams; i++) {
        let img = document.getElementById(`video-${i}`)
        if(mode == 'foscam') {
            img.setAttribute('src', `${ip}cgi-bin/CGIProxy.fcgi?cmd=snapPicture2&usr=admin&pwd=&${Math.floor(Date.now() / 1000)}`)
        }
        // let img = document.getElementById(`video-${i}`)
        // img.setAttribute('src', `http://${ip}:60001/cgi-bin/snapshot.cgi?chn=${i-1}&u=admin&p=&q=0&${Math.floor(Date.now() / 1000)}`)
    }}
    setInterval(func, 1700)
    // }
})