import { useState, useRef } from "react";
import BlogForm from "../components/BlogForm";
import BlogEditor from "../components/BlogEditor";
import EditorToolbar from "../components/EditorToolbar";
import ImageSidebar from "../components/ImageSidebar";

export default function GenerateBlog() {
  const [loading, setLoading] = useState(false);
  const [blogData, setBlogData] = useState(null);
  const [settings, setSettings] = useState({
    title: "",
    tone: "informative",
    language: "English"
  });
  const editorRef = useRef(null);

  const handleInsertImage = (imageUrl) => {
    if (editorRef.current) {
      const editor = editorRef.current;
      editor.model.change((writer) => {
        const imageElement = writer.createElement("imageBlock", {
          src: imageUrl,
        });
        editor.model.insertContent(imageElement, editor.model.document.selection);
      });
    } else {
      alert("Editor is not ready yet!");
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-4 md:p-6">
      <div className="max-w-[1600px] mx-auto">
        <header className="mb-8">
          <h1 className="text-4xl font-extrabold text-gray-900 tracking-tight">
            AI Blog <span className="text-blue-600">Generator</span>
          </h1>
          <p className="text-gray-500 mt-2">Craft SEO-optimized, engaging blogs in seconds.</p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">

          {/* FORM(User fills title,select tone, select language) */}
          <div className="lg:col-span-1 space-y-6">
            <div className="bg-white p-1 rounded-xl shadow-sm border border-gray-100">
              <BlogForm
                setLoading={setLoading}
                setBlogData={setBlogData}
                settings={settings}
                setSettings={setSettings}
              />
            </div>
          </div>

          {/* Editor */}
          <div className="lg:col-span-2 space-y-6">
            <div className="sticky top-6 z-10">
              <EditorToolbar blogData={blogData} />
            </div>
            <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
              <BlogEditor
                loading={loading}
                content={blogData?.content || ""}
                onEditorReady={(editor) => {
                  editorRef.current = editor;
                }}
              />
            </div>
          </div>

          {/* Images Sidebar(To show unsplash and pexels images) */}
          <div className="lg:col-span-1">
            <ImageSidebar
              settings={settings}
              onInsertImage={handleInsertImage}
            />
          </div>
        </div>
      </div>
    </div>
  );
}
