#!/usr/bin/env python3
"""
Upload given notebook to an nbss instance
"""
import argparse
import sys
from pathlib import Path
import requests

def upload_notebook(notebook: Path, enable_annotations: bool, enable_discovery: bool, nbss_url: str):
    """
    Upload a notebook file to an nbss instance with
    """
    upload_url = f"{nbss_url.rstrip('/')}/api/v1/notebook"
    with open(notebook, 'rb') as f:
        print(requests.post(
            upload_url,
            data={
                'enable-annotations': enable_annotations,
                'enable-discovery': enable_discovery
            },
            files={
                'notebook': f,

            }
        ).text)

def main():
    argparser = argparse.ArgumentParser(
        description='Upload notebooks to a NotebookSharingSpace (nbss) instance'
    )
    argparser.add_argument(
        'notebook',
        help='Notebook file to upload',
        type=Path
    )
    argparser.add_argument(
        '--nbss-url',
        default='https://notebooksharing.space',
        help='URL of NotebookSharingSpace instance to upload the notebook to'
    )
    argparser.add_argument(
        '--enable-annotations', '-a',
        action='store_true',
        help='Enable annotations on the notebook with hypothes.is'
    )
    argparser.add_argument(
        '--enable-discovery', '-d',
        action='store_true',
        help='Enable search engines to discover the uploaded notebook'
    )

    args = argparser.parse_args()

    if not args.notebook.exists():
        print(f'File {args.notebook} does not exist, can not upload', file=sys.stderr)
        sys.exit(1)

    upload_notebook(args.notebook, args.enable_annotations, args.enable_discovery, args.nbss_url)

if __name__ == '__main__':
    main()