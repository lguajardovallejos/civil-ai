import React, { useState, useEffect } from "react";
import './App.css'

export default function App() {
  const [normativas, setNormativas] = useState([]);
  const [estadisticas, setEstadisticas] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchNormativas();
  }, []);

  const fetchNormativas = async () => {
    try {
      setLoading(true);
      const response = await fetch('http://localhost:8000/api/normativas');
      if (!response.ok) {
        throw new Error('Error al cargar datos');
      }
      const data = await response.json();
      setNormativas(data.normativas);
      setEstadisticas(data.estadisticas);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const getTipoColor = (tipo) => {
    const colores = {
      'NCh': 'bg-blue-500',
      'AISC': 'bg-green-500',
      'ASCE': 'bg-purple-500',
      'SEI': 'bg-indigo-500',
      'DS': 'bg-orange-500',
      'Otro': 'bg-gray-500'
    };
    return colores[tipo] || 'bg-gray-500';
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-900 flex items-center justify-center">
        <div className="text-white text-xl">Cargando normativas...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-900 flex items-center justify-center">
        <div className="text-red-400 text-xl">Error: {error}</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-4xl font-bold mb-8 text-center">Dashboard de Normativas</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <div className="bg-gray-800 p-6 rounded-lg">
            <h3 className="text-xl font-semibold mb-2">Total Documentos</h3>
            <p className="text-3xl font-bold text-blue-400">{estadisticas.total_documentos || 0}</p>
          </div>
          <div className="bg-gray-800 p-6 rounded-lg">
            <h3 className="text-xl font-semibold mb-2">Normativas Únicas</h3>
            <p className="text-3xl font-bold text-green-400">{estadisticas.normativas_unicas || 0}</p>
          </div>
        </div>

        <div className="bg-gray-800 rounded-lg overflow-hidden">
          <div className="px-6 py-4 border-b border-gray-700">
            <h2 className="text-2xl font-semibold">Normativas Cargadas</h2>
          </div>
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead className="bg-gray-700">
                <tr>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">ID</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Título</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Código</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Institución</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Año</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Tipo</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Chunks</th>
                  <th className="px-6 py-3 text-left text-xs font-medium text-gray-300 uppercase tracking-wider">Fecha Carga</th>
                </tr>
              </thead>
              <tbody className="bg-gray-800 divide-y divide-gray-700">
                {normativas.map((normativa) => (
                  <tr key={normativa.id} className="hover:bg-gray-700">
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300">{normativa.id}</td>
                    <td className="px-6 py-4 text-sm text-gray-300 max-w-xs truncate" title={normativa.titulo}>
                      {normativa.titulo}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300">{normativa.codigo || 'N/A'}</td>
                    <td className="px-6 py-4 text-sm text-gray-300 max-w-xs truncate" title={normativa.institucion}>
                      {normativa.institucion}
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300">{normativa.año}</td>
                    <td className="px-6 py-4 whitespace-nowrap">
                      <span className={`inline-flex px-2 py-1 text-xs font-semibold rounded-full ${getTipoColor(normativa.tipo)}`}>
                        {normativa.tipo}
                      </span>
                    </td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300">{normativa.chunks}</td>
                    <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300">{normativa.fecha_carga}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
