const navElements = document.querySelectorAll('.navbar__item')

navElements.forEach(anchor => {
  anchor.addEventListener('click', e => {
    e.preventDefault()
    const target = anchor.getAttribute('href')

    if (window.location.pathname === target) {
      return
    }

    navElements.forEach(anchor => {
      anchor.classList.remove('navbar__item--selected')
    })

    anchor.classList.add('navbar__item--selected')

    window.history.pushState({}, '', target)

    fetch(target)
      .then(response => response.text())
      .then(html => {
        const parser = new DOMParser()
        const newDocument = parser.parseFromString(html, 'text/html')
        const newContent = newDocument.querySelector('.container')
        document.querySelector('.container').innerHTML = newContent.innerHTML
      })
  })
})
