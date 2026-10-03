/**
 * TecnoAyuda - JavaScript Principal
 * Funcionalidades:
 * - Menú hamburguesa accesible para dispositivos móviles
 * - Interactividad del checklist de mantenimiento del PC
 */

document.addEventListener('DOMContentLoaded', () => {
  // ------------------------------------------------------------------------
  // 1. MENÚ HAMBURGUESA MÓVIL
  // ------------------------------------------------------------------------
  const navToggle = document.getElementById('navToggle');
  const mobileNavPanel = document.getElementById('mobileNavPanel');

  if (navToggle && mobileNavPanel) {
    const toggleMenu = (open) => {
      const isOpen = open !== undefined ? open : !mobileNavPanel.classList.contains('open');
      mobileNavPanel.classList.toggle('open', isOpen);
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      document.body.style.overflow = isOpen ? 'hidden' : '';
    };

    navToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      toggleMenu();
    });

    // Cerrar al hacer clic en un enlace del menú móvil
    const mobileLinks = mobileNavPanel.querySelectorAll('a');
    mobileLinks.forEach((link) => {
      link.addEventListener('click', () => toggleMenu(false));
    });

    // Cerrar al presionar la tecla Escape
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobileNavPanel.classList.contains('open')) {
        toggleMenu(false);
      }
    });

    // Cerrar al hacer clic fuera del menú
    document.addEventListener('click', (e) => {
      if (
        mobileNavPanel.classList.contains('open') &&
        !mobileNavPanel.contains(e.target) &&
        !navToggle.contains(e.target)
      ) {
        toggleMenu(false);
      }
    });
  }

  // ------------------------------------------------------------------------
  // 2. CHECKLIST DE MANTENIMIENTO
  // ------------------------------------------------------------------------
  const checklistForm = document.getElementById('mantenimientoChecklist');
  const checklistCounter = document.getElementById('checklistCounter');
  const btnResetChecklist = document.getElementById('btnResetChecklist');

  if (checklistForm) {
    const checkboxes = checklistForm.querySelectorAll('input[type="checkbox"]');
    const totalTasks = checkboxes.length;

    const updateChecklistProgress = () => {
      let completed = 0;
      checkboxes.forEach((cb) => {
        const item = cb.closest('.checklist-item');
        if (cb.checked) {
          completed++;
          if (item) item.classList.add('done');
        } else {
          if (item) item.classList.remove('done');
        }
      });

      if (checklistCounter) {
        checklistCounter.textContent = `${completed} de ${totalTasks} tareas completadas`;
      }
    };

    // Escuchar cambios en las casillas
    checkboxes.forEach((cb) => {
      cb.addEventListener('change', updateChecklistProgress);
    });

    // Resetear lista de tareas
    if (btnResetChecklist) {
      btnResetChecklist.addEventListener('click', () => {
        checkboxes.forEach((cb) => {
          cb.checked = false;
        });
        updateChecklistProgress();
      });
    }

    // Inicializar estado
    updateChecklistProgress();
  }
});
