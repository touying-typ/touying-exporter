"""cli entry point for touying
"""

import argparse
from . import exporter


def main():
    parser = argparse.ArgumentParser(description="CLI tool for Touying")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subparser for the compile command
    parser_compile = subparsers.add_parser("compile", help="Compile a file")
    parser_compile.add_argument("input", help="Input file")
    parser_compile.add_argument("--output", default=None, help="Output file")
    parser_compile.add_argument(
        "--root", default=None, help="Root directory for typst file"
    )
    parser_compile.add_argument(
        "--font-paths", nargs="*", default=[], help="Paths to custom fonts"
    )
    parser_compile.add_argument(
        "--start-page", type=int, default=1, help="Page to start from"
    )
    parser_compile.add_argument(
        "--count", type=int, default=None, help="Number of pages to convert"
    )
    parser_compile.add_argument(
        "--ppi", type=int, default=500, help="Pixels per inch for PPTX format"
    )
    parser_compile.add_argument(
        "--silent", type=bool, default=False, help="Run silently"
    )
    parser_compile.add_argument(
        "--format",
        choices=["html", "pptx", "pdf", "pdfpc"],
        default="html",
        help="Output format",
    )

    args = parser.parse_args()

    if args.command == "compile":
        if args.format == "html":
            exporter.to_html(
                args.input,
                root=args.root,
                font_paths=args.font_paths,
                output=args.output,
                start_page=args.start_page,
                count=args.count,
                silent=args.silent,
            )
        elif args.format == "pptx":
            exporter.to_pptx(
                args.input,
                output=args.output,
                root=args.root,
                font_paths=args.font_paths,
                start_page=args.start_page,
                count=args.count,
                ppi=args.ppi,
                silent=args.silent,
            )
        elif args.format == "pdf":
            exporter.to_pdf(
                args.input,
                output=args.output,
                root=args.root,
                font_paths=args.font_paths,
                silent=args.silent,
            )
        elif args.format == "pdfpc":
            exporter.to_pdfpc(
                args.input,
                output=args.output,
                root=args.root,
                font_paths=args.font_paths,
                silent=args.silent,
            )
        else:
            raise ValueError(f"Unsupported format: {args.format}")


if __name__ == "__main__":
    main()
