使用py-playwright，包装豆包的脚本

    mkdir doubao-playwright
    cd doubao-playwright/
    python3 -m venv .venv
    source .venv/bin/activate
    
    playwright install
    
    playwright install-deps

playwright codegen  https://www.doubao.com/chat/ --save-storage=auth.json

playwright codegen --load-storage=auth.json  https://www.doubao.com/chat/ 

