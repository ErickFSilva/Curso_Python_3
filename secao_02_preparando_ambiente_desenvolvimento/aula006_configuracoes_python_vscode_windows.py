"""

- Instale o Python 3 e o VSCode;

- Após instalar o python, abra o powershell como administrador e execute o comando abaixo:

    Get-ExecutionPolicy 
        (Padrão: Restricted)
        (Precisa ficar: AllSigned)

    Set-ExecutionPolicy AllSigned -Force


- Em seguida abra o vscode e em seu terminal, na pasta do projeto, execute o comando abaixo para criar o ambiente virtual:

    python -m venv venv
    .\venv\Scripts\activate


- Configurações adicionais do arquivo: settings.json

{
    "workbench.startupEditor": "none",
    "explorer.confirmDragAndDrop": false,
    "explorer.confirmDelete": false,
    "editor.minimap.enabled": false,
    "files.autoGuessEncoding": true,
    "window.menuBarVisibility": "compact",
    "explorer.compactFolders": false,
    "code-runner.executorMap": {
        "javascript": "clear ; node",
        "php": "clear ; php",
        "python": "clear ; python -u",
        "typescript": "clear ; ts-node",
        "sass": "clear ; sass --style expanded",
        "scss": "clear ; scss --style expanded",
        "less": "clear ; cd $dir && lessc $fileName $fileNameWithoutExt.css"
    },
    "code-runner.ignoreSelection": true,
    "code-runner.runInTerminal": true,
    "workbench.iconTheme": "material-icon-theme",
    "python.defaultInterpreterPath": "python"
}

"""