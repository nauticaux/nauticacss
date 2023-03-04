import sass
import rcssmin

compile_array = [
    {"project/core/base.scss": "static/dist/pinta.core.css"},
    {"project/core/responsive-768.scss": "static/dist/pinta.responsive-768.css"},
    {"project/core/responsive-1024.scss": "static/dist/pinta.responsive-1024.css"},
    {"project/core/responsive-1280.scss": "static/dist/pinta.responsive-1280.css"},
    {"project/theming/theming.scss": "static/dist/pinta.theming.css"},
    {"project/components/components.scss": "static/dist/pinta.components.css"},
]

minify_array = [
    {"static/dist/pinta.core.css": "static/dist/pinta.core.min.css"},
    {"static/dist/pinta.responsive-768.css": "static/dist/pinta.responsive-768.min.css"},
    {"static/dist/pinta.responsive-1024.css": "static/dist/pinta.responsive-1024.min.css"},
    {"static/dist/pinta.responsive-1280.css": "static/dist/pinta.responsive-1280.min.css"},
    {"static/dist/pinta.responsive.css": "static/dist/pinta.responsive.min.css"},
    {"static/dist/pinta.theming.css": "static/dist/pinta.theming.min.css"},
    {"static/dist/pinta.components.css": "static/dist/pinta.components.min.css"},
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
