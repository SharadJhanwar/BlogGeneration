import React, { useState } from "react";
import { generateImages } from "../lib/api";

export default function ImageSidebar({ settings, onInsertImage }) {
  const [loading, setLoading] = useState(false);
  const [images, setImages] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");

  const handleGenerateImages = async () => {
    if (!settings.title) {
      alert("Please enter a blog title first");
      return;
    }
    setLoading(true);
    try {
      const data = await generateImages(settings);
      setImages(data.images || []);
    } catch (error) {
      console.error(error);
      alert("Failed to fetch images. Make sure API keys are set in backend .env");
    } finally {
      setLoading(false);
    }
  };

  const handleImageClick = (url) => {
    if (onInsertImage) {
      onInsertImage(url);
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-sm h-fit sticky top-6 scrollbar-thin">
      <h2 className="text-xl font-semibold mb-4">Image Assistant</h2>

      <div className="space-y-4">
        <button
          onClick={handleGenerateImages}
          disabled={loading}
          className="w-full bg-blue-600 text-white p-4 rounded-lg text-center hover:bg-blue-700 transition-colors disabled:bg-blue-300 group"
        >
          <div className="text-3xl mb-2 group-hover:scale-110 transition-transform">
            {loading ? "�" : "✨"}
          </div>
          <p className="text-sm font-medium">{loading ? "Generating..." : "Generate AI Image Suggestions"}</p>
          <p className="text-xs text-blue-100 mt-1">Based on your blog topic & outline</p>
        </button>

        <div className="pt-4 border-t">
          <p className="text-sm font-medium text-gray-700 mb-2">Search Online</p>
          <div className="flex gap-2">
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              placeholder="Search images..."
              className="w-full px-3 py-2 text-sm border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
            />
            <button className="bg-gray-100 text-gray-600 px-3 py-2 rounded-lg text-sm hover:bg-gray-200">
              🔍
            </button>
          </div>
        </div>

        <div className="grid grid-cols-2 gap-3 mt-4">
          {images.map((img, idx) => (
            <div
              key={idx}
              className="relative aspect-square group cursor-pointer overflow-hidden rounded-lg border hover:border-blue-500 shadow-sm"
              onClick={() => handleImageClick(img.url)}
              title={`Photo by ${img.photographer} on ${img.source}. Click to insert into blog.`}
            >
              <img
                src={img.thumb}
                alt={img.source}
                className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
              />
              <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                <span className="text-white text-[10px] font-medium px-2 py-1 bg-black/50 rounded">Insert</span>
              </div>
              <div className="absolute bottom-0 left-0 right-0 p-1 bg-white/80 backdrop-blur-sm text-[8px] truncate">
                {img.source}
              </div>
            </div>
          ))}

          {loading && images.length === 0 && (
            <>
              <div className="aspect-square bg-gray-100 rounded-lg animate-pulse"></div>
              <div className="aspect-square bg-gray-100 rounded-lg animate-pulse"></div>
              <div className="aspect-square bg-gray-100 rounded-lg animate-pulse"></div>
              <div className="aspect-square bg-gray-100 rounded-lg animate-pulse"></div>
            </>
          )}
        </div>

        {images.length > 0 && (
          <p className="text-[10px] text-gray-400 text-center mt-2 italic">
            Click an image to insert it directly into your blog at the cursor position.
          </p>
        )}
      </div>
    </div>
  );
}
