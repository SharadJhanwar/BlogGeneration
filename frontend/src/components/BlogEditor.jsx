import { CKEditor } from "@ckeditor/ckeditor5-react";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";

class Base64UploadAdapter {
  constructor(loader) {
    this.loader = loader;
  }

  upload() {
    return this.loader.file.then(
      (file) =>
        new Promise((resolve, reject) => {
          const reader = new FileReader();
          reader.onload = () => {
            resolve({ default: reader.result });
          };
          reader.onerror = (error) => {
            reject(error);
          };
          reader.readAsDataURL(file);
        })
    );
  }

  abort() {
    // No abort logic needed for local FileReader
  }
}

function MyCustomUploadAdapterPlugin(editor) {
  editor.plugins.get("FileRepository").createUploadAdapter = (loader) => {
    return new Base64UploadAdapter(loader);
  };
}

export default function BlogEditor({ loading, content, onEditorReady }) {
  if (loading) {
    return (
      <div className="bg-white p-6 rounded shadow text-center">
        Generating blog...
      </div>
    );
  }

  if (!content) return null;

  const cleanContent = (data) => {
    if (!data) return "";
    // Remove code blocks
    let cleaned = data.replace(/^```html\s*|```\s*$/g, "").trim();
    return cleaned;
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow space-y-4">
      <h2 className="text-xl font-semibold">Generated Blog</h2>

      <div className="border rounded prose max-w-none">
        <CKEditor
          editor={ClassicEditor}
          data={cleanContent(content)}
          onReady={(editor) => {
            if (onEditorReady) {
              onEditorReady(editor);
            }
          }}
          config={{
            extraPlugins: [MyCustomUploadAdapterPlugin],
            toolbar: [
              "heading",
              "|",
              "bold",
              "italic",
              "link",
              "bulletedList",
              "numberedList",
              "blockQuote",
              "|",
              "imageUpload",
              "insertTable",
              "mediaEmbed",
              "undo",
              "redo",
            ],
          }}
        />
      </div>
    </div>
  );
}
