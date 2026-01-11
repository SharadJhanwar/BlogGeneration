import { useState } from "react";
import { exportBlog, copyToClipboard } from "../lib/editor";

export default function EditorToolbar({ blogData, editorRef }) {
  const [exporting, setExporting] = useState(false);
  const [showDropdown, setShowDropdown] = useState(false);

  if (!blogData) return null;

  const handleCopy = async () => {
    try {
      const currentContent = editorRef.current ? editorRef.current.getData() : blogData.content;
      const textToCopy = currentContent || "";
      await copyToClipboard(textToCopy);
      alert("Copied to clipboard");
    } catch (err) {
      alert("Failed to copy");
    }
  };

  const handleExportClick = async (format) => {
    try {
      setExporting(true);
      setShowDropdown(false);

      const currentContent = editorRef.current ? editorRef.current.getData() : blogData.content;
      const title = blogData.title || "blog_post";

      await exportBlog(currentContent, title, format);
    } catch (error) {
      alert("Failed to export blog");
    } finally {
      setExporting(false);
    }
  };

  return (
    <div className="flex gap-3 items-center">
      <button
        onClick={handleCopy}
        className="px-4 py-2 bg-gray-100 text-gray-700 font-medium rounded-lg hover:bg-gray-200 transition-colors"
      >
        Copy Text
      </button>

      <div className="relative">
        <button
          onClick={() => setShowDropdown(!showDropdown)}
          disabled={exporting}
          className="px-4 py-2 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50 flex items-center gap-2"
        >
          {exporting ? "Exporting..." : "Export"}
          <svg className={`w-4 h-4 transition-transform ${showDropdown ? 'rotate-180' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="19 9l-7 7-7-7" />
          </svg>
        </button>

        {showDropdown && (
          <div className="absolute right-0 mt-2 w-48 bg-white rounded-xl shadow-xl border border-gray-100 py-2 z-50">
            {["PDF", "DOCX", "MD", "HTML"].map((fmt) => (
              <button
                key={fmt}
                onClick={() => handleExportClick(fmt.toLowerCase())}
                className="w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 transition-colors"
              >
                Download as {fmt}
              </button>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
