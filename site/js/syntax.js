// Syntax highlighting using highlight.js (loaded from CDN)
// This file handles code block enhancements

document.addEventListener('DOMContentLoaded', () => {
    // Add copy buttons to code blocks
    document.querySelectorAll('pre code').forEach((block) => {
        const pre = block.parentElement;
        const wrapper = document.createElement('div');
        wrapper.className = 'code-block-wrapper';

        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);

        const button = document.createElement('button');
        button.className = 'copy-button';
        button.textContent = 'Copy';

        button.addEventListener('click', async () => {
            const code = block.textContent;

            try {
                await navigator.clipboard.writeText(code);
                button.textContent = 'Copied!';
                button.classList.add('copied');

                setTimeout(() => {
                    button.textContent = 'Copy';
                    button.classList.remove('copied');
                }, 2000);
            } catch (err) {
                console.error('Failed to copy code:', err);
                button.textContent = 'Error';
                setTimeout(() => {
                    button.textContent = 'Copy';
                }, 2000);
            }
        });

        wrapper.appendChild(button);
    });

    // Add language labels
    document.querySelectorAll('pre code[class*="language-"]').forEach((block) => {
        const match = block.className.match(/language-(\w+)/);
        if (match) {
            const language = match[1];
            const label = document.createElement('span');
            label.className = 'code-language-label';
            label.textContent = language;
            block.parentElement.insertBefore(label, block);
        }
    });
});
