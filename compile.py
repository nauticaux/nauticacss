import sass
import rcssmin

compile_array = [
    {"project/layout/main.scss": "dist/pinta.layout.css"},
    {"project/layout/responsive-768.scss": "dist/pinta.responsive-768.css"},
    {"project/layout/responsive-1024.scss": "dist/pinta.responsive-1024.css"},
    {"project/layout/responsive-1280.scss": "dist/pinta.responsive-1280.css"},
    {"project/theming/theming.scss": "dist/pinta.theming.css"},
    {"project/components/components.scss": "dist/pinta.components.css"},
]

minify_array = [
    {"dist/pinta.layout.css": "dist/min/pinta.layout.min.css"},
    {"dist/pinta.responsive-768.css": "dist/min/pinta.responsive-768.min.css"},
    {"dist/pinta.responsive-1024.css": "dist/min/pinta.responsive-1024.min.css"},
    {"dist/pinta.responsive-1280.css": "dist/min/pinta.responsive-1280.min.css"},
    {"dist/pinta.theming.css": "dist/min/pinta.theming.min.css"},
    {"dist/pinta.components.css": "dist/min/pinta.components.min.css"},
]


def compile_sass(sass_array):
    for file in sass_array:
        for source, dest in file.items():
            with open(dest, "w") as outfile:
                outfile.write(sass.compile(filename=source))
            print(f"{source} compiled to {dest}")


def minify_css(css_array):
    for file in css_array:
        for source, dest in file.items():
            with open(source, "r") as infile:
                with open(dest, "w") as outfile:
                    outfile.write(rcssmin.cssmin(infile.read()))
            print(f"{source} minified to {dest}")


if __name__ == '__main__':
    compile_sass(compile_array)
    minify_css(minify_array)
