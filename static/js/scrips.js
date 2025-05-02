custom_sliderbar = document.getElementById('admin-slider-bar')
custom_btn_activate_sliderbar = document.getElementById('custom-btn-activate-sliderbar')
item_click_d_none = document.querySelectorAll('.d-block')


link = document.querySelectorAll('#link')
nav_link = document.getElementById('nav-link')

let status_slider_bar = false;

for (let i of item_click_d_none) {
    i.classList.toggle('d-none')
}


custom_btn_activate_sliderbar.onclick = () => {
    
    custom_sliderbar.classList.toggle('admin-slider-bar-open')
    custom_sliderbar.classList.toggle('admin-slider-bar-close')
  

    for (let i of link) {
        i.classList.toggle('flex-column')
        i.classList.toggle('fs-9')
        i.classList.toggle('fs-6')
    }
    
    nav_link.classList.toggle('px-2')
    nav_link.classList.toggle('px-1')
}