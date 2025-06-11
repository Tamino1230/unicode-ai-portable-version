import re

class PortableVersion:
    def __init__(self):
        self.version = "0.1.0"
        self.name = "Portable Version"
        self.description = "A portable version of the application."
        self.author = "Tamino1230"
        
        #! Programmvars
        self.removed = False

        self.unicode_chars_to_remove = [
            '\u200b',  # Zero Width Space
            '\u200c',  # Zero Width Non-Joiner
            '\u200d',  # Zero Width Joiner
            '\uFEFF',  # Zero Width No-Break Space
            '\u2060',  # Word Joiner
            '\u180E',  # Mongolian Vowel Separator
            '\u202A',  # LRE
            '\u202B',  # RLE
            '\u202C',  # PDF
            '\u202D',  # LRO
            '\u202E',  # RLO
            '\u00AD',  # Soft Hyphen
            '\u034F',  # Combining Grapheme Joiner
            '\u061C',  # Arabic Letter Mark
            '\u115F',  # Hangul Filler
            '\u1160',  # Hangul Jungseong Filler
            '\u17B4',  # Khmer Vowel Inherent Aq
            '\u17B5',  # Khmer Vowel Inherent Aa
            '\u180B',  # Mongolian Free Variation Selector One
            '\u180C',  # Mongolian Free Variation Selector Two
            '\u180D',  # Mongolian Free Variation Selector Three
            '\uFE00',  # Variation Selector-1
            '\uFE01',  # Variation Selector-2
            '\uFE02',  # Variation Selector-3
            '\uFE03',  # Variation Selector-4
            '\uFE04',  # Variation Selector-5
            '\uFE05',  # Variation Selector-6
            '\uFE06',  # Variation Selector-7
            '\uFE07',  # Variation Selector-8
            '\uFE08',  # Variation Selector-9
            '\uFE09',  # Variation Selector-10
            '\uFE0A',  # Variation Selector-11
            '\uFE0B',  # Variation Selector-12
            '\uFE0C',  # Variation Selector-13
            '\uFE0D',  # Variation Selector-14
            '\uFE0E',  # Variation Selector-15
            '\uFE0F',  # Variation Selector-16
            '\uFFF9',  # Interlinear Annotation Anchor
            '\uFFFA',  # Interlinear Annotation Separator
            '\uFFFB',  # Interlinear Annotation Terminator
        ]

        self.commands = {
            "help": "Displays help information.",
            "--version": "Returns the current version of the application.",
            "--v": "Returns the current version of the application (alias).",
            "clean": "Removes specific Unicode characters from a given text or file.",
            "char": "Shows the current list of characters to remove.",
        }

    def _get_file_content(self, file_path):
        try:
            with open(file_path, 'rb') as file:
                raw = file.read()
            try:
                return raw.decode('utf-8')
            except UnicodeDecodeError:
                return raw.decode('latin1')
        except FileNotFoundError:
            return None
        
    def _write_file_content(self, file_path, content):
        try:
            with open(file_path, 'w', encoding='utf-8', newline='') as file:
                file.write(content)
            return True
        except Exception as e:
            print(f"Error writing to file {file_path}: {e}")
            return False

    def parse_portable_remove_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            chars = [c.strip() for c in content.split(',') if c.strip()]
            parsed_chars = []
            for c in chars:
                if c.startswith('\\u') or c.startswith('\\U'):
                    try:
                        parsed_chars.append(bytes(c, "utf-8").decode("unicode_escape"))
                    except Exception:
                        parsed_chars.append(c)
                else:
                    parsed_chars.append(c)
            return parsed_chars
        except Exception as e:
            return None

    def clean_unicode_chars(self, text: str, replace_with="", use_file_chars=None, count_stats=False):
        if not text:
            return "No text provided to clean."
        chars_to_remove = use_file_chars if use_file_chars is not None else self.unicode_chars_to_remove
        stats = {char: 0 for char in chars_to_remove}
        for char in chars_to_remove:
            try:
                real_char = bytes(char, "utf-8").decode("unicode_escape")
            except Exception:
                real_char = char
            count = text.count(char) + text.count(real_char)
            stats[char] = count
            text = text.replace(char, replace_with).replace(real_char, replace_with)
        if count_stats:
            return text, stats
        return text

    def get_version(self):
        return f"PortableEXE 'unicode-ai' v{self.version}"
    
    def print_current_chars(self):
        if not self.unicode_chars_to_remove:
            return "No characters to remove."
        chars = ", ".join(repr(char) for char in self.unicode_chars_to_remove)
        return f"Current characters to remove: {chars}"

    def help(self):
        help_text = "Available commands:\n"
        help_text += "\nclean <text>\n    Removes invisible/untypable Unicode characters from the given text.\n"
        help_text += "clean --file <path> [--usefile] \n    Cleans a file in-place.\n    - The file is read, all invisible/untypable Unicode characters are removed,\n      and the file is overwritten with the cleaned, human-readable result.\n    - If --usefile is given, the list of characters to remove is loaded from .portable (comma-separated, supports Unicode escapes).\n    - A summary of removed characters is printed.\n"
        help_text += "\nchar\n    Shows the current list of characters to remove.\n"
        help_text += "\n--version or --v\n    Shows the current version.\n"
        help_text += "help\n    Shows this help message.\n"
        help_text += "\nNotes:\n  - The default removal list includes all common invisible, zero-width, and AI/ChatGPT Unicode artifacts.\n  - .portable (if used) must be in the same folder as this script.\n  - All commands are case-sensitive.\n"
        return help_text.strip()
    
    def add_char_to_remove(self, char: str):
        if char and char not in self.unicode_chars_to_remove:
            self.unicode_chars_to_remove.append(char)
            return f"Character '{char}' added to removal list."
        return f"Character '{char}' is already in the removal list or invalid."

    def remove_char_from_remove(self, char: str):
        if char in self.unicode_chars_to_remove:
            self.unicode_chars_to_remove.remove(char)
            return f"Character '{char}' removed from removal list."
        return f"Character '{char}' not found in removal list."

    def to_unicode_escape(self, text):
        return ''.join(f'\\u{ord(c):04X}' if ord(c) <= 0xFFFF else f'\\U{ord(c):08X}' for c in text)

    def from_unicode_escape(self, text):
        try:
            return bytes(text, "utf-8").decode("unicode_escape")
        except Exception:
            return text

    def run(self, command, *args):
        if not command:
            return "Usage: no-ai <command> [args]\nType 'help' for available commands."
        if command == "help":
            return self.help()
        elif command in ("--version", "--v"):
            return self.get_version()
        elif command == "clean":
            use_file = False
            file_path = None
            text_args = []
            i = 0
            while i < len(args):
                arg = args[i]
                if arg in ("--usefile", "--portable"):
                    use_file = True
                elif arg == "--file" and i + 1 < len(args):
                    file_path = args[i + 1]
                    i += 1
                else:
                    text_args.append(arg)
                i += 1
            chars_from_file = None
            if use_file:
                chars_from_file = self.parse_portable_remove_file(".portable")
                if chars_from_file is None:
                    return "Could not read .portable or file is invalid."
            if file_path:
                content = self._get_file_content(file_path)
                if content is None:
                    return f"Could not read file: {file_path}"
                # Step 1: Convert to Unicode-Escapes
                content = self.to_unicode_escape(content)
                # Step 2: Remove unwanted Unicode characters
                cleaned, stats = self.clean_unicode_chars(content, use_file_chars=chars_from_file, count_stats=True)
                # Step 3: Convert back to normal text
                cleaned = self.from_unicode_escape(cleaned)
                # Step 4: Write back to file
                success = self._write_file_content(file_path, cleaned)
                summary = "\nSummary of removed characters:\n"
                for char, count in stats.items():
                    summary += f"{repr(char)}: {count} removed\n"
                if success:
                    return f"File cleaned and overwritten: {file_path}{summary}"
                else:
                    return f"Failed to write cleaned content to {file_path}{summary}"
            elif text_args:
                text = " ".join(text_args)
                cleaned, stats = self.clean_unicode_chars(text, use_file_chars=chars_from_file, count_stats=True)
                summary = "\nSummary of removed characters:\n"
                for char, count in stats.items():
                    summary += f"{repr(char)}: {count} removed\n"
                return cleaned + summary
            else:
                return "Please provide text or use --file <path> to clean a file."
        elif command == "char":
            if not args:
                return self.print_current_chars()
            else:
                return "Usage: char"
        else:
            return f"Unknown command: {command}"
        
if __name__ == "__main__":
    import sys
    portable = PortableVersion()
    if len(sys.argv) < 2:
        print("Usage: unicode-ai <command> [args]\nType 'help' for available commands.")
    else:
        command = sys.argv[1]
        args = sys.argv[2:]
        result = portable.run(command, *args)
        if isinstance(result, str):
            try:
                for line in result.splitlines():
                    sys.stdout.buffer.write((line + '\n').encode('utf-8', errors='replace'))
            except Exception:
                print(result)
        else:
            print(result)
