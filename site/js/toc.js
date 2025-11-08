// Table of Contents

const content = document.querySelector('.markdown-body');
const tocNav = document.getElementById('tableOfContents');

if (content && tocNav) {
    // Get all headings
    const headings = content.querySelectorAll('h2, h3');

    if (headings.length > 0) {
        const tocList = document.createElement('ul');
        tocList.className = 'toc-list';

        headings.forEach((heading, index) => {
            // Add ID if not present
            if (!heading.id) {
                heading.id = `heading-${index}`;
            }

            // Create TOC item
            const li = document.createElement('li');
            li.className = `toc-item toc-${heading.tagName.toLowerCase()}`;

            const link = document.createElement('a');
            link.href = `#${heading.id}`;
            link.textContent = heading.textContent.replace(/#$/, '').trim();
            link.className = 'toc-link';

            li.appendChild(link);
            tocList.appendChild(li);
        });

        tocNav.appendChild(tocList);

        // Highlight current section on scroll
        let activeLink = null;

        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        const id = entry.target.id;
                        const newActiveLink = tocNav.querySelector(`a[href="#${id}"]`);

                        if (newActiveLink && newActiveLink !== activeLink) {
                            if (activeLink) {
                                activeLink.classList.remove('active');
                            }
                            newActiveLink.classList.add('active');
                            activeLink = newActiveLink;
                        }
                    }
                });
            },
            {
                rootMargin: '-80px 0px -80% 0px'
            }
        );

        headings.forEach((heading) => {
            observer.observe(heading);
        });

        // Smooth scroll
        tocNav.addEventListener('click', (e) => {
            if (e.target.tagName === 'A') {
                e.preventDefault();
                const id = e.target.getAttribute('href').slice(1);
                const element = document.getElementById(id);

                if (element) {
                    const offset = 80;
                    const bodyRect = document.body.getBoundingClientRect().top;
                    const elementRect = element.getBoundingClientRect().top;
                    const elementPosition = elementRect - bodyRect;
                    const offsetPosition = elementPosition - offset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            }
        });
    }
}
