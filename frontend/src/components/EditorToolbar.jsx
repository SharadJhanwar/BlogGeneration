export default function EditorToolbar({ blogData }) {
  if (!blogData) return null;

  const copyToClipboard = () => {
    const textToCopy = blogData.content || "";
    navigator.clipboard.writeText(textToCopy);
    alert("Copied to clipboard");
  };

  return (
    <div className="flex gap-3">
      <button
        onClick={copyToClipboard}
        className="px-4 py-2 bg-black text-white rounded"
      >
        Copy
      </button>
    </div>
  );
}
