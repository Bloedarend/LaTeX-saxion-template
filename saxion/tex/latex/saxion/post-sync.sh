PREFIX="saxion: "

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYGMENTIZE_DIR="$SCRIPT_DIR/pygmentize"

register_pygmentize() {
    if [ ! -d "$PYGMENTIZE_DIR" ]; then
        echo "$PREFIX No pygmentize directory found at $PYGMENTIZE_DIR."
        return 1
    fi

    if [ ! -f "$PYGMENTIZE_DIR/setup.py" ]; then
        echo "$PREFIX setup.py not found in $PYGMENTIZE_DIR."
        return 1
    fi

    echo "$PREFIX Registering custom Pygments style from $PYGMENTIZE_DIR ..."
    (
        cd "$PYGMENTIZE_DIR" || exit 1
        if pip install .; then
            echo "$PREFIX ✅ Pygments style registered successfully."
        else
            echo "$PREFIX ❌ Failed to register Pygments style."
            return 1
        fi
    )
}

register_pygmentize
