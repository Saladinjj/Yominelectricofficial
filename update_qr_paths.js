const fs = require('fs');
const path = require('path');
const glob = require('glob');

// Using the provided workspace root
const rootDir = 'C:/Users/Saladin/Desktop/yominelectric-main';
const newPath = '/assets/images/qr-wechat.jpg';

// Pattern for old paths
const oldPaths = [
    /\/assets\/img\/wechat-qr\.png/g,
    /assets\/img\/wechat-qr\.png/g,
    /assets\/wechat-qr\.jpg/g,
    /\/wechat-qr\.jpg/g
];

function updateFiles() {
    // Search for all html, js, css files
    const files = fs.readdirSync(rootDir, { recursive: true })
        .filter(f => {
            const ext = path.extname(f);
            return (ext === '.html' || ext === '.js' || ext === '.css') && !f.includes('node_modules');
        });

    files.forEach(f => {
        const fullPath = path.join(rootDir, f);
        if (fs.lstatSync(fullPath).isDirectory()) return;

        let content = fs.readFileSync(fullPath, 'utf8');
        let original = content;

        oldPaths.forEach(re => {
            content = content.replace(re, newPath);
        });

        if (content !== original) {
            fs.writeFileSync(fullPath, content, 'utf8');
            console.log(`Updated: ${f}`);
        }
    });
}

updateFiles();
